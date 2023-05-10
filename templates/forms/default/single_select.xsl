<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        
        <xsl:variable name="identifier" select="single-select/identifier" />
        
        <div class="container">
            <div class="form-group">
                
                <label for="{$identifier}">
                    <xsl:value-of select="single-select/label"/> 
                </label>
                
                <xsl:if test="single-select/query">
                    <select class="form-control form-control-sm" 
                            name="{$identifier}" id="{$identifier}">
                        <option></option>
                    </select>
                </xsl:if>
                
                <xsl:if test="single-select/options">
                    <select class="form-control form-control-sm" 
                            name="{$identifier}" id="{$identifier}">       
                        <xsl:for-each select="single-select/options/option">
                            <xsl:variable name="optionValue" select="value" />
                            <option value="{$optionValue}">
                                <xsl:value-of select="value"/>
                            </option>
                        </xsl:for-each>
                    </select>
                </xsl:if>
                
                <small class="form-text form-text-sm text-muted">
                    <xsl:value-of select="single-select/tooltip"/>
                </small>
                
            </div>
        </div>
        
    </xsl:template>
</xsl:stylesheet>
