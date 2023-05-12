<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        
        <xsl:variable name="identifier" select="simple-textbox/identifier" />
        <xsl:variable name="maxLength" select="simple-textbox/max-length" />
        
        <div class="container mt-2">
            <div class="form-group">
                
                <label for="{$identifier}">
                    <xsl:value-of select="simple-textbox/label"/> 
                </label>
                
                <input type="text" class="form-control form-control-sm" 
                       id="{$identifier}" maxlength="{$maxLength}"
                       name="{$identifier}"/>
                
                <small class="form-text form-text-sm text-muted">
                    <xsl:value-of select="simple-textbox/tooltip"/>
                </small>
                
            </div>
        </div>
        
    </xsl:template>
</xsl:stylesheet>
