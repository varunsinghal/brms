<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        
        <xsl:variable name="identifier" select="checkbox/identifier" />
        <xsl:variable name="checkedValue" select="checkbox/checked-value" />
        
        <div class="container mt-2">
            <div class="form-group">
                
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" 
                           value="{$checkedValue}" id="{$identifier}"
                           name="{$identifier}" />
                    <label class="form-check-label" for="{$identifier}">
                        <xsl:value-of select="checkbox/label"/>
                    </label>
                </div>
                
                <small class="form-text form-text-sm text-muted">
                    <xsl:value-of select="checkbox/tooltip"/>
                </small>
                
            </div>
        </div>
        
    </xsl:template>
</xsl:stylesheet>
